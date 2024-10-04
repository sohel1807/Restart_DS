Regularization

Definition:
Regularization is the technique of adding additional information (or constraints) to a model to prevent overfitting.

Types:

Ridge (L2)

Lasso (L1)

Elastic Net (Combination of L2 and L1)


Purpose:
Regularization helps solve the problem of overfitting by adding penalties to the model coefficients, reducing their magnitude.


---

Overfitting

Explanation:
Overfitting occurs when a model performs exceptionally well on the training set but fails to generalize to unseen test data. This is usually due to the model being too complex and overly fitted to the noise in the training data.

Characterized by:

High variance in predictions.

In terms of a simple equation:
 (where  is the slope or coefficient).
If  is too large, it makes  too dependent on , causing overfitting.


Solution:
Regularization reduces overfitting by controlling the magnitude of the model coefficients, ensuring the model generalizes better.


---

Ridge Regression (L2 Regularization)

Main Advantages:

Effectively handles overfitting by adding a penalty based on the size of coefficients.

Handles multicollinearity, which occurs when features are highly correlated, by distributing weights more evenly.

Preferred when you want to retain all features in the model without eliminating any.


Mechanism:
Ridge regression adds a penalty equal to the sum of the squared coefficients to the cost function. This ensures that large coefficients are penalized, preventing the model from becoming too dependent on any one feature.

Loss Function:

\text{Loss} = \text{Loss\_function} + \lambda \sum_{i=1}^{n} m_i^2

Key Point:
Ridge regression never reduces coefficients to zero, unlike Lasso, meaning it retains all features but shrinks the coefficients.


---

Impact of the Regularization Parameter 

Range:
 can range from 0 to infinity.

Low  (close to 0): Behaves like standard linear regression, with minimal regularization. The model fits the training data more closely.

High  (close to infinity): Increases the penalty on large coefficients, potentially leading to underfitting, where the model becomes too simple and loses its predictive power.



---

When to Prefer Ridge Over Lasso?

Choose Ridge when:

You want to keep all features in the model.

Multicollinearity exists between the features, and you want to distribute the impact of correlated features.

You want to reduce overfitting without shrinking any coefficient to zero.
