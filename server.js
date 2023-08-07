import express from "express";
import recipeRouter from "./routes/recipeRouter.js"
import logger from 'morgan';

const app = express();
const port = 3000;

app.use(express.json());
app.use(recipeRouter);
app.use(logger('dev'));

app.use(express.static("client"));
app.use("/post", express.static("client/post"));


app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});