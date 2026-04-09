# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-desktop-setup-labwc
Version:        20260324
Release:        %autorelease
Summary:        Preset labwc configuration for openRuyi desktop user
License:        MIT
BuildArch:      noarch
VCS:            git:https://git.openruyi.cn/openRuyi/openruyi-desktop-setup-labwc
#!RemoteAsset
Source0:        https://git.openruyi.cn/openRuyi/openruyi-desktop-setup-labwc/archive/%{version}.tar.gz

Requires:       labwc
Requires:       wofi
Requires:       sfwbar
Requires:       swaybg
Requires:       waybar
Requires:       foot
Requires:       shared-mime-info
Requires:       fonts-fontawesome

%description
Preset labwc configuration files for desktop users.
This package installs system-wide defaults for labwc under
${XDG_CONFIG_DIRS:-/etc/xdg}/labwc.

%prep
%autosetup -T -c
tar -xzf %{SOURCE0} --strip-components=1

%build

%install
install -d %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/labwc
install -d %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/waybar
install -d %{buildroot}%{_sysconfdir}/xdg/labwc
install -m 0644 openruyi.png %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/labwc/openruyi.png
install -m 0644 waybar/config.jsonc %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/waybar/config.jsonc
install -m 0644 waybar/style.css %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/waybar/style.css
install -m 0644 waybar/power_menu.xml %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/waybar/power_menu.xml
install -m 0644 rc.xml %{buildroot}%{_sysconfdir}/xdg/labwc/rc.xml
install -m 0644 menu.xml %{buildroot}%{_sysconfdir}/xdg/labwc/menu.xml
install -m 0755 autostart %{buildroot}%{_sysconfdir}/xdg/labwc/autostart

%posttrans
install -d %{_sysconfdir}/xdg/waybar
install -m 0644 %{_datadir}/openruyi-desktop-setup-labwc/waybar/config.jsonc %{_sysconfdir}/xdg/waybar/config.jsonc
install -m 0644 %{_datadir}/openruyi-desktop-setup-labwc/waybar/style.css %{_sysconfdir}/xdg/waybar/style.css
install -m 0644 %{_datadir}/openruyi-desktop-setup-labwc/waybar/power_menu.xml %{_sysconfdir}/xdg/waybar/power_menu.xml

%files
%{_datadir}/openruyi-desktop-setup-labwc/labwc/openruyi.png
%{_datadir}/openruyi-desktop-setup-labwc/waybar/config.jsonc
%{_datadir}/openruyi-desktop-setup-labwc/waybar/style.css
%{_datadir}/openruyi-desktop-setup-labwc/waybar/power_menu.xml
%{_sysconfdir}/xdg/labwc/rc.xml
%{_sysconfdir}/xdg/labwc/menu.xml
%{_sysconfdir}/xdg/labwc/autostart

%changelog
%autochangelog
