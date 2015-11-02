extern crate iron;
extern crate router;

use iron::{Iron, Request, Response, IronResult};
use iron::status;
use router::{Router};

fn main() {
    let mut router = Router::new();
    router.get("/", handler);
    router.get("/:query", handler);

    Iron::new(router).http("localhost:3000").unwrap();

    fn handler(req: &mut Request) -> IronResult<Response> {
        let ref query = req.extensions.get::<Router>()
            .unwrap().find("query").unwrap_or("/");
        Ok(Response::with((status::Ok, *query)))
    }
}
