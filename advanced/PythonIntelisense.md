# Python code editors

One of the most common discussions while teaching RaspberryPi Python programming was editing code using Visual Code and the squiggly line appearing underneath the code, suggesting mistakes or improvements.  It looks like the python language is slowly modernizing and adding the IDE support tooling and files required. This is a manual step and requires manual intervention via python [Stub files](https://www.python.org/dev/peps/pep-0561/) and IDE plugins that include language support.  

```Powershell
# Option 1
python -c "import os, sys; print(os.path.dirname(sys.executable))"

# Option 2
cmd
where python
```

## References

[Visual Code IntelliSense upgrade](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
[Pylance - Introduction](https://devblogs.microsoft.com/python/announcing-pylance-fast-feature-rich-language-support-for-python-in-visual-studio-code/)
[Pylance - GPIO support](https://github.com/microsoft/pylance-release/issues/974)
[TypeShed - Community driven stub files](https://github.com/python/typeshed/tree/master/stubs)
[Python Stub file generator](https://mypy.readthedocs.io/en/stable/stubgen.html)
[Python Package Manager - GPIO](https://pypi.org/project/RPi.GPIO/)
[Python and GPIO Code examples](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/)
[Extend Python with C](https://docs.python.org/3/extending/extending.html)
