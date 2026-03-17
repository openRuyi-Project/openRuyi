# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-desktop-setup-labwc
Version:        20260321
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
install -d %{buildroot}%{_sysconfdir}/xdg/labwc
install -m 0644 openruyi.png %{buildroot}%{_datadir}/openruyi-desktop-setup-labwc/labwc/openruyi.png
install -m 0644 rc.xml %{buildroot}%{_sysconfdir}/xdg/labwc/rc.xml
install -m 0644 menu.xml %{buildroot}%{_sysconfdir}/xdg/labwc/menu.xml
install -m 0755 autostart %{buildroot}%{_sysconfdir}/xdg/labwc/autostart

%files
%{_datadir}/openruyi-desktop-setup-labwc/labwc/openruyi.png
%config(noreplace) %{_sysconfdir}/xdg/labwc/rc.xml
%config(noreplace) %{_sysconfdir}/xdg/labwc/menu.xml
%config(noreplace) %{_sysconfdir}/xdg/labwc/autostart

%changelog
%{?autochangelog}
