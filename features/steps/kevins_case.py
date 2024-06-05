from ast import And
from operator import contains
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('the user launches elucidat page')
def step_given_user_on_elucidat_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(5)


@when('the user presses start')
def step_when_user_presses_start(context):
    context.driver.find_element(By.ID, "pa_5c9126fe3b767_p15577f075e9-button__text").click()
    


@then('they should see both crime cases')
def step_then_user_should_see_cases(context):
    time.sleep(3)  
    #Kevins case
    context.driver.find_element(By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-caption__text-1").is_displayed()
    time.sleep(3)
    #Other case
    context.driver.find_element(By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-caption__text-2").is_displayed()
    # clicking kevins case 
    context.driver.find_element(By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-caption__text-1").click()
    time.sleep(5)
    #Kevins crime video is displayed
    context.driver.find_element(By.ID, "pa_5c9126fe434ba_p154ce332d27-text").is_displayed()
    


@when('user chooses to judge kevins case')
def step_when_user_chooses_kevins_case(context):
    #clicking "judge this" on kevins case
    context.driver.find_element(By.ID, "pa_5c9126fe434ba_p15564daa856-textButton").click()
    time.sleep(3)
    #guilty and not guilty buttons displayed 
    context.driver.find_element(By.ID, "pa_5c9126fe47260_p15515116385-answer-1").is_displayed()
    context.driver.find_element(By.ID, "pa_5c9126fe47260_p15515116385-answer-2").is_displayed()


@when('user votes Kevin is guilty')
def step_when_user_chooses_kevins_guilty(context):
    #chooses that Kevin is guilty
    context.driver.find_element(By.ID, "pa_5c9126fe47260_p15515116385-answer-1").click()
    time.sleep(3)
    # clicking "vote"
    context.driver.find_element(By.ID, "pa_5c9126fe47260_p15515116385-button__text").click()


@then('user gets confirmation of choice')
def step_then_user_sees_wrong_choice_confirmation(context):
    time.sleep(3)
    #user sees opposite of what they choose 
    context.driver.find_elements(By.XPATH, "//*[contains(text(), 'NOT GUILTY!')]") 
    # context.driver.quit()


@when('user continues to explore the evidence')
def step_when_user_continues_to_evidence(context):
    #presses continue on confirmation popup
    context.driver.find_element(By.ID, "pa_5c9126fe47260_p15583b88249-button__text").click()
    time.sleep(3)
    # Explore the evidence is displayed - check for text
    context.driver.find_element(By.ID, "pr_5c9126fd760e5_p155729036fa-page__title").is_displayed()  

@when('user views evidence they see popup')
def step_when_user_views_evidence(context):
    #presses on fingerprint evidence - check for text
    context.driver.find_element(By.ID, "pa_5c9126fe4b742_p1554fa6d6c6-explorer__item--button-1").click()
    time.sleep(3)
    # Explore the evidence is displayed
    context.driver.find_elements(By.ID, "pa_5c9126fe4b742_p1554fa6d7d7-modalTitle-1")

@when('user closes popup and continues to decision')
def step_when_user_continues_to_decision(context):
    #presses close on fingerprint popup
    context.driver.find_element(By.ID, "pa_5c9126fe4b742_p15583bfb7a0-dismiss_button-1").click()
    time.sleep(3)
    # presses continue on envidence page 
    context.driver.find_element(By.ID, "pa_5c9126fe4b742_p15550a254a1-textButton").click()


@then('user lands on the you decide page & continues')
def step_then_user_sees_you_decide_page(context):
    time.sleep(3)
    #user sees you decide page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'YOU DECIDE')]").is_displayed()

    #continue button is displayed
    context.driver.find_element(By.ID, "pa_5c9126fe4f952_p15578944323-button__text").is_displayed()
    #continue button is clicked
    context.driver.find_element(By.ID, "pa_5c9126fe4f952_p15578944323-button__text").click()

    
@when('user decides if fingerprints are reliable')
def step_when_user_assess_fingerprints(context):
    time.sleep(3)
    #user lands on the fingerprint page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE FINGERPRINT')]").is_displayed()

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe5331b_p15578a164ba-button__text-front").click()
    prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p15578a165c1-text")
    prosecution_argument.is_displayed()   
    assert prosecution_argument.is_displayed(), '"We were able to recover a partial print from the bin and following analysis, we feel very confident that it matches the suspect’s."' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe5331b_p15578a136b2-button__text-front").click()
    defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p15578a137c0-text")
    defence_argument.is_displayed()   
    assert defence_argument.is_displayed(), '“Fingerprint analysis relies on a human comparing one set of patterns with another, so there is room for error. It’s possible for fingerprint ‘experts’ to find a match when there isn’t one.”' 
    time.sleep(3)

    #user decides fingerprints can be reliable
    can_be_reliale_option = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p155cc4e94a5-card__image-3")
    can_be_reliale_option.click()

    #user submits vote
    fingerprint_vote = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p155cc4e94a5-save_button")
    fingerprint_vote.click()

    #expert popup is displayed
    expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p155cc4e95cb-modal__header")
    expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe5331b_p155cc4e96eb-button__text")
    continue_btn.click()



@when('user decides DNA is reliable')
def step_when_user_assess_dna(context):
    time.sleep(3)
    #user lands on the fingerprint page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE DNA')]").is_displayed()
    time.sleep(3)

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe57197_p15578a164ba-button__text-front").click()
    dna_prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe57197_p15578a165c1-text")
    dna_prosecution_argument.is_displayed()   
    assert dna_prosecution_argument.is_displayed(), '“You can’t argue with DNA evidence. The DNA belonged to Kevin and no one else.”' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe57197_p15578a136b2-button__text-front").click()
    dna_defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe57197_p15578a137c0-text")
    dna_defence_argument.is_displayed()   
    assert dna_defence_argument.is_displayed(), '“There could be any number of ways that Kevin’s DNA came to be there.”' 
    time.sleep(3)

    #user decides fingerprints can be reliable
    can_be_reliale_option = context.driver.find_element(By.ID, "pa_5c9126fe57197_p155cc4e94a5-card__image-3")
    can_be_reliale_option.click()

    #user submits vote
    dna_vote = context.driver.find_element(By.ID, "pa_5c9126fe57197_p155cc4e94a5-save_button")
    dna_vote.click()

    #expert popup is displayed
    dna_expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe57197_p155cc4e95cb-modal__header")
    dna_expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe57197_p155cc4e96eb-button__text")
    continue_btn.click()
    


@when('user decides if hair sample is reliable')
def step_when_user_assess_hair(context):
    time.sleep(3)
    #user lands on the fingerprint page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE HAIR SAMPLE')]").is_displayed()
    time.sleep(3)

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe5b173_p15578a164ba-button__text-front").click()
    hair_prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p15578a165c1-text")
    hair_prosecution_argument.is_displayed()   
    assert hair_prosecution_argument.is_displayed(), '“Expert analysis on a hair recovered from the scene showed that it had many markers matching a hair taken from the suspect. Our experts agree this is very strong evidence that the hair belonged to Kevin.”' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe5b173_p15578a136b2-button__text-front").click()
    hair_defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p15578a137c0-text")
    hair_defence_argument.is_displayed()   
    assert hair_defence_argument.is_displayed(), '“Microscopic hair analysis is not a validated scientific technique and is not based on sound scientific data.”' 
    time.sleep(3)

    #user decides fingerprints can be reliable
    may_be_reliale_option = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p155cc4e94a5-card__image-2")
    may_be_reliale_option.click()

    #user submits vote
    hair_vote = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p155cc4e94a5-save_button")
    hair_vote.click()

    #expert popup is displayed
    hair_expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p155cc4e95e6-modal__header")
    hair_expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe5b173_p155cc4e970b-button__text")
    continue_btn.click()    




@when('user decides if footprint is reliable')
def step_when_user_assess_footprint(context):
    time.sleep(3)
    #user lands on the fingerprint page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE FOOTPRINT')]").is_displayed()
    time.sleep(3)

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p15578a164ba-button__text-front").click()
    footprint_prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p15578a165c1-text")
    footprint_prosecution_argument.is_displayed()   
    assert footprint_prosecution_argument.is_displayed(), '“The footprint was clear enough that we were able to take an impression and determine that the shoe was a size 12. Given the similarities, and that his fingerprints were also found at the scene, it is very likely that it belongs to him.”' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p15578a136b2-button__text-front").click()
    footprint_defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p15578a137c0-text")
    footprint_defence_argument.is_displayed()   
    assert footprint_defence_argument.is_displayed(), '“All this shows is that someone with the same size shoes as Kevin was in the area. It’s hardly a rare size, so this provides only a very weak link to Kevin.”' 
    time.sleep(3)

    #user decides fingerprints can be reliable
    may_be_unreliale_option = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p155cc4e94a5-card__image-1")
    may_be_unreliale_option.click()

    #user submits vote
    footprint_vote = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p155cc4e94a5-save_button")
    footprint_vote.click()

    #expert popup is displayed
    footprint_expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p155cc4e95cb-modal__header")
    footprint_expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe5f2c1_p155cc4e96eb-button__text")
    continue_btn.click() 



@when('user decides if confession is reliable')
def step_when_user_assess_confession(context):
    time.sleep(3)
    #user lands on the fingerprint page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE CONFESSION')]").is_displayed()
    time.sleep(3)

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe631c0_p15578a164ba-button__text-front").click()
    confession_prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p15578a165c1-text")
    confession_prosecution_argument.is_displayed()   
    assert confession_prosecution_argument.is_displayed(), '“He confessed to committing the crime. There’s no way anyone would admit to committing a murder if they didn’t actually do it.”' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe631c0_p15578a136b2-button__text-front").click()
    confession_defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p15578a137c0-text")
    confession_defence_argument.is_displayed()   
    assert confession_defence_argument.is_displayed(), '“Kevin only confessed after many hours of relentless interrogation!”' 
    time.sleep(3)

    #user decides footprints can be reliable
    can_be_reliale_option = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p155cc4e94a5-card__image-3")
    can_be_reliale_option.click()

    #user submits vote
    confession_vote = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p155cc4e94a5-save_button")
    confession_vote.click()

    #expert popup is displayed
    confession_expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p155cc4e95e6-modal__header")
    confession_expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe631c0_p155cc4e970b-button__text")
    continue_btn.click()  


@when('user decides if eyewitness is reliable')
def step_when_user_assess_eyewitness(context):
    time.sleep(3)
    #user lands on the eyewitness page 
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'THE EYEWITNESS')]").is_displayed()
    time.sleep(3)

    #user can press flip to see the prosecution argument 
    context.driver.find_element(By.ID, "pa_5c9126fe671e0_p15578a164ba-button__text-front").click()
    eyewitness_prosecution_argument = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p15578a165c1-text")
    eyewitness_prosecution_argument.is_displayed()   
    assert eyewitness_prosecution_argument.is_displayed(), '“We have two witness who saw Kevin fleeing the scene and who picked him out of a line-up.”' 
    time.sleep(3)


    #user can press flip to see the defence argument
    context.driver.find_element(By.ID, "pa_5c9126fe671e0_p15578a136b2-button__text-front").click()
    eyewitness_defence_argument = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p15578a137c0-text")
    eyewitness_defence_argument.is_displayed()   
    assert eyewitness_defence_argument.is_displayed(), '“Kevin does not dispute being in the area, so it is possible the witnesses recognised him because they had seen him that night.”' 
    time.sleep(3)

    #user decides eyewitness can be reliable
    can_be_reliale_option = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p155cc4e94a5-card__image-3")
    can_be_reliale_option.click()

    #user submits vote
    eyewitness_vote = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p155cc4e94a5-save_button")
    eyewitness_vote.click()

    #expert popup is displayed
    eyewitness_expert_popup = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p155cc4e95e6-modal__header")
    eyewitness_expert_popup.is_displayed()

    continue_btn = context.driver.find_element(By.ID, "pa_5c9126fe671e0_p155cc4e970b-button__text")
    continue_btn.click()



@when('user must make final vote')
def step_then_user_makes_final_vote(context):
    time.sleep(3)

    # user lands on final vote page
    final_vote_page = context.driver.find_element(By.ID, "pa_5c9126fe6af70_p154cdf68524-text")
    final_vote_page.is_displayed()   
    assert final_vote_page.is_displayed(), 'Now you’ve had a chance to look at the evidence in a bit more detail...'

    #user decides user is not guilty
    not_guilty_btn = context.driver.find_element(By.ID, "pa_5c9126fe6af70_p15515116385-answer-2")
    not_guilty_btn.click()
    
    #vote button is clicked
    final_vote_btn = context.driver.find_element(By.ID, "pa_5c9126fe6af70_p15515116385-button__text")
    final_vote_btn.click()

    final_vote_popup = context.driver.find_element(By.ID, "pa_5c9126fe6af70_p1554e60707e-modalTitle")
    final_vote_popup.is_displayed()   
    assert final_vote_popup.is_displayed(), 'Not guilty!'
    time.sleep(3)

    # user clicks continue btn
    cont_btn = context.driver.find_element(By.ID, "pa_5c9126fe6af70_p15583b685ad-button__text")
    cont_btn.click()



@then('user sees what actually happened')
def step_then_user_sees_what_happened(context):
    time.sleep(3)

    # user lands on final vote page
    context.driver.find_element(By.ID, "pa_5c9126fe6ea48_paw").is_displayed()   


    #user clicks final verdict
    final_verdict_btn = context.driver.find_element(By.ID, "pa_5c9126fe6ea48_p15564daa856-button__text")
    final_verdict_btn.click()
    time.sleep(3)


    #user sees final verdict
    final_verdict_reveal = context.driver.find_element(By.ID, "pa_5c9126fe72755_p1557df9c9aa-projectTitle")
    final_verdict_reveal.is_displayed()   
    assert final_verdict_reveal.is_displayed(), 'NOT GUILTY!'

   

    context.driver.quit()   




#could have autonated other case
#coould have expanded to view what research said 
#could have viewed the real life cases studies when the final verdict is revealed


#readme - pre reqs, how to run, what I automated, what I would have done with more time, some manual issues I found through out the project