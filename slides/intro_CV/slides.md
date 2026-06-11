---
title: "Intro to Computer Vision"
author: "Michiel Bontenbal & Rick van Kersbergen"
date: "2026-09-04"
description: "First lecture for the Master Applied Artificial Intelligence Expert Workshops."
---

## Master Applied Artificial Intelligence Expert Workshops -- Session 1 Lecturers Michiel  Bontenbal , MSc Rick van Kersbergen, MSc {#slide-1}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

## Agenda {#slide-2}

::: {.smartart .vProcess5 layout="vProcess5"}
:::

## Introduction  Tech Workshop Curriculum {#slide-3}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

## Slide 4

  No.   Date         Lecturer         Subjects
  ----- ------------ ---------------- --------------------------------------------------------------------------
  1     Thu ? Sep    Rick + Michiel   AI assisted coding, Data exploration, Faces
  2     Thu ? Sep   Michiel          Object Detection, Video, CNN advanced
  3     Thu ? Sep   Rick             Evaluations, Build an app 
  4     Thu ? Sep   Michiel          Embeddings (SSL, CLIP, Search) &  preparation tech reviews
  5     Thu ? Oct    Rick + Michiel   Tech reviews
  6     Thu ? Oct    Rick             ML  Ops  + onderwerpen  obv  vragen studenten
  7     Thu ? Oct   Michiel          Vision Language Models (VLM's) +  onderwerpen   obv   vragen   studenten

## Slide 5

Vragenbox op DLO

![Afbeelding met tekst, schermopname, software, Lettertype

Door AI gegenereerde inhoud is mogelijk onjuist.](slides/intro_CV/assets/ppt/media/image6.png "Afbeelding 3")

## Slide 6

Techreview

- Assessment on the technical aspect of your project  up till that point.  Outcomes  A2, B1, B2, B3, C2
- You hand in on the DLO:

<!-- -->

- Relevant part of your project report (see study guide)
- Link to your up-to-date Git repo (make it navigable)

<!-- -->

- See it as a feedbackmoment on your progress, not as a test
- 

<!-- -->

- 

## Slide 7

Usage of Generative AI within this module

- AI Assessment Scale Level 3:  AI mag gebruikt worden ter  ondersteuning  bij specifieke taken. Je wordt altijd verplicht om AI-gegenereerde content kritisch te evalueren en indien nodig aan te passen (Zie Techworkshop DLO)
- Verantwoording van keuzes in eigen woorden om begrip aan te kunnen tonen -- Gen AI niet toegestaan voor  schrijven  uiteindelijke uitleg in rapport.
- 

## AI  assisted   Coding {#slide-8}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

## Slide 9

AI Assisted Coding in VS Code

![](slides/intro_CV/assets/ppt/media/image7.png "Picture 4")

\<\-- Try a different model!

## Slide 10

Do you get the right response?   'Alignment'

Prompt 

Response

![Brain in head outline](slides/intro_CV/assets/ppt/media/image8.png "Graphic 8")

![Brain in head outline](slides/intro_CV/assets/ppt/media/image8.png "Graphic 9")

Intro to Alignment:  https://aligned.substack.com/p/what-is-alignment , blog by Jan  Leike

LLM

![Gegenereerde afbeelding](slides/intro_CV/assets/ppt/media/image10.png "Picture 2")

## Slide 11

Tips for better prompting in AI coding

Prompt 

Response

![Brain in head outline](slides/intro_CV/assets/ppt/media/image8.png "Graphic 8")

![Brain in head outline](slides/intro_CV/assets/ppt/media/image8.png "Graphic 9")

LLM

W rite a  better  prompt

- Think   before   you  prompt
- 
- Try  different prompts
- 
- For  beginnners ,  you   can   add  ' write   simple  code ...'
- 

- 

Understand  the  response

- Be  aware  of mistakes. 
- 
- Ask   questions  like " Explain   this  code  to  me "
- 
- Decide   if   you  want  to   use   the  code or start  again   with  a  differerent  prompt. 

![Gegenereerde afbeelding](slides/intro_CV/assets/ppt/media/image10.png "Picture 2")

![Arrow circle with solid fill](slides/intro_CV/assets/ppt/media/image11.png "Graphic 16")

iterate

## Slide 12

![Gegenereerde afbeelding](slides/intro_CV/assets/ppt/media/image13.png "Picture 2")

Human -- AI 

pair programming

Work together with the AI, your new best buddy!

The AI can make mistakes, you have to guide it. Do not give up.

## Slide 13

But  remember   active   learning  is  better !  

Eg.  writing code is more effective than reading code.  Why?

- 

<!-- -->

- 

<!-- -->

- You remember it better
- You are more critical
- You are more engaged

## Slide 14

![undefined](slides/intro_CV/assets/ppt/media/image14.jpeg "Picture 2")

![](slides/intro_CV/assets/ppt/media/image15.png "Picture 3")

![](slides/intro_CV/assets/ppt/media/image16.jpeg "Picture 4")

First  learn   to  walk  before   you   learn   to  run!

## Slide 15

To  do / exercises

Beginners:

- Set up  Copilot  in VS Code ( ask   your   favorite  AI  to  help  you  out)
- Write code  to   calculate   fibonacci   numbers  
- 

Experienced

- Compare  code  from :

<!-- -->

- Claude.ai  vs   Copilot
- Try   uploading   an  image  to   create  code
- Try   to   create  a front-end app  with  HTML / JS / CSS (= multiple files)
- 

- 

## Slide 16

![Afbeelding met tekst, schermopname, software, Webpagina

Door AI gegenereerde inhoud is mogelijk onjuist.](slides/intro_CV/assets/ppt/media/image17.png "Afbeelding 2")

## Data Exploration  and   Initial  Analysis {#slide-17}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

A2

B1

D1

## Je stelt voor een AI-oplossing juridische, ethische, organisatorische, functionele en technische  requirements  op. {#slide-18}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

A2

B1

D1

Je verkent en prepareert een dataset voor het trainen en testen van een AI-model en kan de voor- en nadelen van het gebruik van een bestaande dataset onderbouwen, rekening houdend met technische en ethische randvoorwaarden.

Je verzamelt en verwerkt actief feedback over de eigen kennis, vaardigheden en ontwikkeling en laat zien deze feedback te kunnen gebruiken om je werk te verbeteren.

## The life-cycle of  MLOps : CRISPML(Q) {#slide-19}

![Afbeelding met tekst, schermopname, Lettertype, nummer

Door AI gegenereerde inhoud is mogelijk onjuist.](slides/intro_CV/assets/ppt/media/image18.png "Afbeelding 5")

## Choosing a dataset {#slide-20}

- Always first concern  yourself   with   Data  Provenance

<!-- -->

- Source,  collection   process ,  might   any  of these  be   biased ?

<!-- -->

- Then , check  Data  Description

<!-- -->

- Size , Contents, Label  quality  ( especially  target feature  for   age   estimation !)

<!-- -->

- 
- Where ?

<!-- -->

- Similar  Research,  Kaggle ,  Huggingface

## Initial Exploration and  Visualisation {#slide-21}

- Visualisation   is  an   integral   part of  the  data  exploration   phase !
- You\'ll   probably  first want  to  look at different  distributions

<!-- -->

- Feature  distributions ,  Bivariate /Multivariate  exploration
- Use histograms, boxplots, scatterplots, etc.

<!-- -->

- Also check more technical details

<!-- -->

- Target leaking
- image quality (resolution, brightness, cropping issues)
- Label noise (incorrect ages, approximations)

<!-- -->

- Ask yourself  what makes this data predictive?

## Data bias when using people {#slide-22}

- Algorithms do  not  care about your data at all!

<!-- -->

- They just want to \'win\' by solving your problem

<!-- -->

- Winning in this case is minimizing your chosen loss function

<!-- -->

- By finding any pattern that might contribute to this

<!-- -->

- Representation is therefore  unimaginably  important

## Slide 23

![Afbeelding met Menselijk gezicht, collage, vrouw, person

Door AI gegenereerde inhoud is mogelijk onjuist.](slides/intro_CV/assets/ppt/media/image19.png "Afbeelding 7")

## Feature Engineering {#slide-24}

- When you know your data, you can start engineering
- Possible engineering steps:

<!-- -->

- Face alignment / Cropping
- Grayscaling
- Over- and  Undersampling  of classes
- Normalisation  of the data for simpler representations
- Regression vs Classification framing
- 

<!-- -->

- Don\'t just ask yourself  what,  but more importantly  why

## Other important subjects: {#slide-25}

- Data leakage / test data invalidation (I can\'t stress you enough about this)
- Data splitting strategies (random, stratified,  etc )
- Think already about evaluation metrics (MAE, RMSE, Fairness metrics)
- Reproducability  of your workflow

<!-- -->

- And the iterative nature of it ( learning outcome B4)

## Practicum \~ 45 min {#slide-26}

- Make groups of four students (avoid your project members). As a group, perform data analysis on the  UTKFace  dataset (see notebook on DLO). 
- 
- In general, answer:  what can we say about this data, and which feature engineering steps might be necessary? Use data  visualisations !
- 
- Some questions to get you started:

<!-- -->

- Distribution:  What distributions should be checked? Are they balanced or skewed?
- Quality : Any errors, anomalies, missing data, unrealistic images,  etc
- Bias : What kind of biases are present? How would you fix these?
- Image inspection : What factors might mess with prediction? Lighting, angles, cropping  etc

<!-- -->

- In the end we recap:

<!-- -->

- Surprises? Concerns? Take-aways for the project?

## Faces {#slide-27}

![](slides/intro_CV/assets/ppt/media/image5.emf "Tijdelijke aanduiding voor afbeelding 3")

## Slide 28

![Aging Time Lapse Comparison - Science of Age Gender & Race](slides/intro_CV/assets/ppt/media/image20.jpeg "Online Media 3")

## Python packages {#slide-29}

  No   Name                Description                           Link
  ---- ------------------- ------------------------------------- ----------------------------------------------
  1    MTCNN               A  CNN model for face detection       https://pypi.org/project/mtcnn/  
  2    Deepface            A CNN model  for   age   estimation   https://pypi.org/project/deepface/
  3    F ace-recognition                                         https:// pypi.org /project/face-recognition/

In Python it is relatively easy to create a package / library.

Below three examples for faces.

## Exercise  notebooks {#slide-30}

Gezichtsdetectie_with \_ cnn .ipynb

Age_estimation \_ Deepface .ipynb
