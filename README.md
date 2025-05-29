# analyses_friends_annotations
# Friends annotations analysis project for brainhack school 2025:

## Background
This project is based on the friends annotations dataset, which contains half-episodes that are annotated.
The goal of these annotations are to give context about the visual stimuli (FRIENDS half-episodes) that were shown
to participants in a fmri. This dataset is also one of the dataset available for the Algonauts challenge, where participants use the stimuli data and the brain response data to create brain encoding models.

Here are some questions that encoding models attempt to address that I took from the MAIN educational website :

"Does the variation in the response depend on the stimulus?

How well do the responses ‘encode’ the stimuli?

How well are the responses ‘explained’ by the stimuli?

Can some responses be explained by specific stimuli?

How can we quantify the dependence of responses on the stimuli?" (The MAIN Educational Team, 2024)

Having good robust annotations and analyses on the stimuli acts as a good base to anser these types of questions.   

## Main goal
The main goal of this brainhack project is to do basic statistical analyses to the friends annotations data and to present
the results in the form of visualisations. These analyses will provide better context and information about the visual stimuli on different levels of analyses (season, episodes, scenes, segments, frames). Ultimately, to understand what happens when humans view multi-modal stimuli like a video, we need 
descriptions of each stimuli type (visual, transcript, narrative, emotions etc. ). With the available annotations in the annotations dataset, that are mainly visual, this project will try to be a good foundation for future inquiry about the other types stimuli modalities. Doing cross-modal correlations between the emotions and visuals could be one of the many possible future analyses to better understand video media, tv, cinema and our brains.

## Learning goals:
I plan to use this project to learn how to group data into panda dataframes and use visualisation tools to plot the data included in clean datasets. I will also try to learn how to write efficient code using functions. Building a website presenting my final analyses is also one of my learning goals.

## Data used
Theses analyses are made on the friends annotations dataset, it is available as a submodule in this repo.

[https://github.com/courtois-neuromod/friends_annotations.git]

This dataset contains annotations made for season one to six of FRIENDS and it contains for every half-episode:

Number of scene cuts (PYScene): Ai model that detects scene cuts.

Number of local maxima and location of maximum in pixel space (saliency with deepgazemr):  model trained to predict the likelihood of the viewer's gaze position for each movie frame.

Segments annotations (manual annotations): Segments where annotated by a person. It gives detail about onset and offset of each segments depending on their 
modalities (location change, character entry etc.)

Transcript (Speech2text): AssemblyAI speech-to-text transcription. Produces time-stamped movie transcripts.

## Main analyses 
Plot different relations between scenes, segments, duration, frames, number of local maximas and more!

Types of plots: barplots for frequencies, barplots for proportions and hexbins for density visualisations

Here's an example of a plot contained in this dataset: 

![download](https://github.com/user-attachments/assets/d19ff0c2-9cc2-42e7-82ae-ff1a9a57dd6d)

## Tools
The tools I will use are 

   Jupyter notebooks to organize my analysis and create some interactive plots.
   
   python,

   git and github to version control and share my analyses
   
   mystmd to create my website to promote this dataset and present it in a neat way

## Python libraries
Pandas: This tool will be useful to concatenate data about different half-episodes togheter

matplotlib, seaborn and numpy: These tools are useful to plot barplots, hexbin plots and distributions

## End product
The end product will be a website containing a description of the project and the plots.

![alt text](https://i.pinimg.com/736x/fb/d5/3a/fbd53a0dc2a88bcad9d25986cb42964c.jpg)

## Deliverables
Notebooks on github, website


<a href="https://github.com/cleode5a7">
   <img src="https://avatars.githubusercontent.com/u/210581839?v=4?s=100" width="100px;" alt=""/>
   <br /><sub><b>cléo</b></sub>
</a>
