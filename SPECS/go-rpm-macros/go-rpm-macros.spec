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
URL:            https://github.com/openRuyi-Project/go-rpm-macros
#!RemoteAsset:  sha256:a7e328684503191c82d2c7a4c56030783e51f9f9f8b1f6f7800714230692f960
Source0:        https://github.com/openRuyi-Project/go-rpm-macros/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

%description
This package provides RPM macros for packaging Go software in openRuyi.

%prep
%autosetup -n %{name}-%{version}

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
