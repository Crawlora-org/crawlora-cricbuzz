use crawlora_cricbuzz::{Client, CricbuzzMatchesParams, ModelCricbuzzMatchesResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .cricbuzz
        .matches(CricbuzzMatchesParams {
            ..Default::default()
        })
        .await?;
    let data: ModelCricbuzzMatchesResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
