**SENG 438- Software Testing, Reliability, and Quality**

**Lab. Report \#5 – Software Reliability Assessment**

| Group \#:  28        |
| ----------------- |
| Student Names:      |
| John            |   
| Mark            |   
| Ron             |   
| Lana            |   

# Introduction



# Assessment Using Reliability Growth Testing 

Plot of the original data:

![dqawadw](https://github.com/user-attachments/assets/a40bffc9-05e9-4fc6-9933-887bcd115b76)

We started by selecting all the hazard functions to look into all the possible models based on the original plot of data. 
![ggg](https://github.com/user-attachments/assets/dafdf043-5171-4dc9-8521-8bc8343ea635)


Going to the model comparison tab, we can see a sorted table. We select to sort log-likelihood to choose our 2 best model. Log likelihood is the natural algorithm for the likelihood function, the likelihood function measures the probability of the observed data given certain parameters. The higher the log-likelihood, the better the model fits the data. 
![afoaifwn](https://github.com/user-attachments/assets/127f19bb-4fe8-4f60-82e0-765eee1b0260)


by sorting it, we see that DW3 (F, C) and IFRGSB (F, C) have the highest log-likelihood with our original failure data.
![ss](https://github.com/user-attachments/assets/72943855-dab1-4091-963a-d5bf6145d1dc)


Here is the graph of IFRGSB (F, C) alone with our base failure data
![ggfa](https://github.com/user-attachments/assets/ca8dd264-0da6-46e4-95cf-df4f9ef2b362)


Here is the graph of DW3 (F, C) alone with our base failure data
![sx z](https://github.com/user-attachments/assets/4fbef495-0a5c-4d97-bcec-2e9d38f09d0e)




This is the failure intensity and reliablilty graph as well as the two chosen predicted models. 
![ggasd](https://github.com/user-attachments/assets/8ba13b57-f883-4a03-9942-91e6191ab809)


Here is the reliability graph of DW3 model alone with original failure data 
![bhxcv](https://github.com/user-attachments/assets/fcbc965b-19cf-4345-9465-0343d1f8fc82)


Here is the reliability graph of IFRGSB (F, C) model alone with original failure data 
![bbzx](https://github.com/user-attachments/assets/60ef5cfd-3741-40bb-8065-1563aec756c7)


By analyzing the reliability graph that was from our data, we know that we have 367 cumulative failure counts. These failure counts occured in the span 73 weeks. By doing (367/73), we get 5.02 failure rate. Now we just need to set the intensity target to 4.00 or something lower. This will give us a visual on how each model predicts and how long till we reach the failure target
![jjj](https://github.com/user-attachments/assets/feae00ef-f610-4d2a-9521-317d8d457fcf)



# Assessment Using Reliability Demonstration Chart 
MTTFmin original (MTTFmin = 1500000)

<img width="436" alt="Screenshot 2025-04-10 at 1 39 50 PM" src="https://github.com/user-attachments/assets/178efca4-a264-4ace-9e4b-695e2e202a8b" />

MTTFmin half (MTTFmin = 750000)

<img width="437" alt="Screenshot 2025-04-10 at 1 40 09 PM" src="https://github.com/user-attachments/assets/cfd04afb-e628-4af7-b008-4bb63654e474" />

MTTFmin doubled (MTTFmin = 3000000)

<img width="437" alt="Screenshot 2025-04-10 at 1 39 33 PM" src="https://github.com/user-attachments/assets/941039bb-9d3a-4f55-87a1-0f16a345fffd" />




# 

# Comparison of Results
In part 1, the Reliabilty Growth Testing shows that the ... In part 2, the Reliability Demostration Charts shows that the system only requires more testing if the MTTFmin of the same is very large. However, the system can be considered acceptable at normal MTTFmin values.

# Discussion on Similarity and Differences of the Two Techniques
Both reliability growth testing and the reliability demonstration chart try to find out how reliable a system is based on failure data, but they have different ways to approach the problem. They both share a common goal, which is helping engineers understand whether a system is meeting its reliability goals and if more testing is required. Both use plots to visualize failures and they require failure data collected during integration testing. Reliability growth testing, focuses on tracking improvements in reliability over time, its more detailed and provides metrics such as failure rate, mean time to failure, and reliability curves and supports model selection and comparison. While RDC is simpler, it is an excel based tool that helps determine if a system meets a minimum reliability requirement, it is better used for determining whether the system is good enough to move forward.  While growth testing requires more structured data and offers in depth analysis, RDC is easier to use with basic failure time inputs and is great for fast visualizing.

# How the team work/effort was divided and managed

# 

# Difficulties encountered, challenges overcome, and lessons learned

# Comments/feedback on the lab itself
