# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-sarasa-gothic
Version:        1.0.37
Release:        %autorelease
Summary:        Sarasa font families
License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
VCS:            git:https://github.com/be5invis/Sarasa-Gothic
#!RemoteAsset:  sha256:608ba9cd77d20277a9eea290e2c36dc40054883c09bf35f942d89476e6041dbe
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/Sarasa-TTC-%{version}.zip
Source1:        LICENSE
BuildArch:      noarch

BuildRequires:  unzip

%description
Sarasa is a CJK composite font family based on Inter, Iosevka, and Source Han Sans.

This package contains hinted Sarasa TTC font collections.

%prep
%autosetup -c
cp %{SOURCE1} LICENSE

%build
# No build required

%install
mkdir -p %{buildroot}%{_datadir}/fonts/truetype
install -m 0644 -p Sarasa-*.ttc %{buildroot}%{_datadir}/fonts/truetype/

%files
%license LICENSE
%{_datadir}/fonts/truetype/Sarasa-*.ttc

%changelog
%autochangelog
