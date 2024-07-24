import renderer from "react-test-renderer";
import Graph from "./Graph";

describe("<Graph />", () => {
  it("renders correctly", () => {
    const tree = renderer.create(<Graph />).toJSON();
    expect(tree).toMatchSnapshot();
  });
  it("has 1 child", () => {
    const tree = renderer.create(<Graph />).toJSON();
    expect(tree.children.length).toBe(1);
  });
});
