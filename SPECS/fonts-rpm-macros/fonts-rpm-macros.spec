# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-rpm-macros
Version:        20260625
Release:        %autorelease
Summary:        RPM macros for font packages
License:        MIT
Source0:        macros.fonts
BuildArch:      noarch

%description
This package contains macros which are used when building font packages.
It provides path macros for font directories and convenience macros
for installing font files to the correct locations.

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.fonts

%files
%{_rpmconfigdir}/macros.d/macros.fonts

%changelog
%autochangelog
