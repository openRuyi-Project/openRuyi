# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           go-rpm-macros
Version:        0.1
Release:        %autorelease
Summary:        Go macros for openRuyi packaging
License:        MIT
# TODO: Update the URL when there is a proper project page
URL:            https://git.openruyi.cn/misaka00251/go-rpm-macros
#!RemoteAsset
Source0:        https://git.openruyi.cn/misaka00251/go-rpm-macros/archive/v%{version}.tar.gz
BuildArch:      noarch

%description
This package provides RPM macros for packaging Go software in openRuyi.

%prep
%autosetup -n %{name}

# No build needed
%build

%install
install -D -m644 macros.golang %{buildroot}%{_rpmmacrodir}/macros.golang
install -D -m644 macros.buildsystem.golang %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golang
install -D -m644 macros.buildsystem.golangmodules %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golangmodules

# No check needed
%check

%files
%license LICENSE
%{_rpmmacrodir}/macros.golang
%{_rpmmacrodir}/macros.buildsystem.golang
%{_rpmmacrodir}/macros.buildsystem.golangmodules

%changelog
%autochangelog
