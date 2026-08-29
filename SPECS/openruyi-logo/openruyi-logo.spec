# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-logo
Version:        2026.06
Release:        %autorelease
Summary:        Logo of openRuyi
License:        CC-BY-SA-4.0
URL:            https://github.com/openRuyi-Project/openRuyi-logo
#!RemoteAsset:  sha256:2a51e67da14b555bc50617520a09d0ce8557c13400693ed1ffd9378e7f4eee89
Source0:        https://github.com/openRuyi-Project/openRuyi-logo/releases/download/2026.06/openRuyi.zip#/%{name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip

Requires:       hicolor-icon-theme

%description
This package provides the logo for openRuyi.

%prep
%autosetup -c

%build

%install
for size in 16 24 32 48 64 72 96 128 256 512 1024; do
    install -Dpm0644 icon_${size}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/openRuyi.png
done

install -Dpm0644 openRuyi.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openRuyi.svg

%check

%files
%license LICENSE
%{_datadir}/icons/hicolor/*/apps/openRuyi.png
%{_datadir}/icons/hicolor/scalable/apps/openRuyi.svg

%changelog
%autochangelog
