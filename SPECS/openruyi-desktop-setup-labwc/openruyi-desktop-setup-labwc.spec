# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-desktop-setup-labwc
Version:        20261124
Release:        %autorelease
Summary:        Preset labwc configuration for openRuyi desktop user
License:        MIT
BuildArch:      noarch
VCS:            git:https://github.com/openRuyi-Project/openruyi-desktop-setup-labwc
#!RemoteAsset:  sha256:f7f474e13b521676509a90ea7719fc2452681aa012893d6ee0bcf21940ffeea7
Source0:        https://github.com/openRuyi-Project/openruyi-desktop-setup-labwc/archive/refs/tags/%{version}.tar.gz

BuildRequires:  systemd-rpm-macros

Requires:       labwc >= 0.20
Requires:       systemd
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
%autosetup -n openruyi-desktop-setup-labwc-%{version}

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
install -m 0755 shutdown %{buildroot}%{_sysconfdir}/xdg/labwc/shutdown
install -D -m 0644 systemd/waybar.service.d/50-openruyi-labwc.conf \
    %{buildroot}%{_userunitdir}/waybar.service.d/50-openruyi-labwc.conf

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
%{_sysconfdir}/xdg/labwc/shutdown
%dir %{_userunitdir}/waybar.service.d
%{_userunitdir}/waybar.service.d/50-openruyi-labwc.conf

%changelog
%autochangelog
