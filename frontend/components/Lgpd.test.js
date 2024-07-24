import renderer from "react-test-renderer";
import Lgpd from "./Lgpd";

describe("<Lgpd />", () => {
  it("renders correctly", () => {
    const tree = renderer.create(<Lgpd />).toJSON();
    expect(tree).toMatchSnapshot();
  });
  it("has 1 child", () => {
    const tree = renderer.create(<Lgpd />).toJSON();
    expect(tree.children.length).toBe(1);
  });
});
