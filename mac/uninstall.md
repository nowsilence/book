** Java卸载 **

```
sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin 
sudo rm -fr /Library/PreferencesPanes/JavaControlPanel.prefpane

ls /Library/Java/JavaVirtualMachines/ 
输出：jdk-9.0.1.jdk

sudo rm -rf /Library/Java/JavaVirtualMachines/jdk-9.0.1.jdk
```