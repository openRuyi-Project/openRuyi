# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qt6-macros
Version:        20251130
Release:        %autorelease
Summary:        RPM macros for Qt6 packages
License:        MIT
Source0:        macros.qt6

Requires:       cmake
Requires:       ninja

%description
This package provides macros which are used by Qt6 packages.

%prep

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.qt6

%files
%{_rpmmacrodir}/macros.qt6

%changelog
%autochangelog
