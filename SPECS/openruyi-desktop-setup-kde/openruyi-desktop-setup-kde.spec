# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-desktop-setup-kde
Version:        202603
Release:        %autorelease
Summary:        openRuyi default wallpaper override for KDE Plasma
License:        MIT
BuildArch:      noarch
URL:            https://openruyi.cn/
VCS:            git:https://github.com/openRuyi-Project/openruyi-desktop-wallpapers
#!RemoteAsset:  sha256:5a75e3f67a731b3c559ea7e86b6f0f3f1e93df4734b3f91b6eef4aad9862e5d2
Source0:        https://github.com/openRuyi-Project/openruyi-desktop-wallpapers/archive/refs/tags/%{version}.zip

BuildRequires:  unzip
BuildRequires:  kf6-extra-cmake-modules

Requires:       plasma-workspace
Requires:       plasma-desktop
Requires:       plasma-session
Requires:       plasma5support
Requires:       systemsettings
Requires:       konsole
Requires:       dolphin
Requires:       kf6-kwindowsystem
Requires:       kf6-kcoreaddons
Requires:       kf6-kcmutils
Requires:       kf6-kconfig
Requires:       kf6-qqc2-desktop-style

Recommends:     discover
Recommends:     mpv
Recommends:     falkon
Recommends:     sddm

%description
Set openRuyi wallpaper as the KDE Plasma default by overriding the
upstream default image in the Next wallpaper package path.

%prep
%autosetup -n openruyi-desktop-wallpapers-%{version}

%install
install -d %{buildroot}%{_datadir}/openruyi-desktop-setup-kde
install -d %{buildroot}%{_kf6_sharedir}/wallpapers

install -m 0644 %{version}/openruyi.png \
  %{buildroot}%{_datadir}/openruyi-desktop-setup-kde/openruyi.png

install -m 0644 %{version}/* \
  %{buildroot}%{_kf6_sharedir}/wallpapers/

%posttrans
install -d %{_datadir}/wallpapers/Next/contents/images
install -m 0644 %{_datadir}/openruyi-desktop-setup-kde/openruyi.png %{_datadir}/wallpapers/Next/contents/images/4096x2160.png
install -m 0644 %{_datadir}/openruyi-desktop-setup-kde/openruyi.png %{_datadir}/wallpapers/Next/contents/images/5120x2880.png

%files
%{_datadir}/openruyi-desktop-setup-kde/openruyi.png
%{_kf6_sharedir}/wallpapers/

%changelog
%autochangelog
