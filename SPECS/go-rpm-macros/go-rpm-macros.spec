# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           go-rpm-macros
Version:        0.3
Release:        %autorelease
Summary:        Go macros for openRuyi packaging
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/openRuyi-Project/go-rpm-macros
#!RemoteAsset:  sha256:5709153834da251f9ad1b98c3ee45ee44a519fc1a6e07749eded9a5acf2dbdd2
Source0:        https://github.com/openRuyi-Project/go-rpm-macros/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  go
# for tests
BuildRequires:  rpm-build

%description
This package provides RPM macros for packaging Go software in openRuyi.

%prep
%autosetup -n %{name}-%{version}

# No build needed
%build

%install
install -D -m644 go.attr %{buildroot}%{_fileattrsdir}/go.attr
install -D -m755 go-rpm-integration %{buildroot}%{_rpmconfigdir}/go-rpm-integration
install -D -m644 macros.golang %{buildroot}%{_rpmmacrodir}/macros.golang
install -D -m644 macros.buildsystem.golang %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golang
install -D -m644 macros.buildsystem.golangmodules %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golangmodules

%check
./tests/test-go-submodules.sh

%files
%doc LICENSES.md
%license LICENSE LICENSE.GPL-3.0-or-later
%{_fileattrsdir}/go.attr
%{_rpmconfigdir}/go-rpm-integration
%{_rpmmacrodir}/macros.golang
%{_rpmmacrodir}/macros.buildsystem.golang
%{_rpmmacrodir}/macros.buildsystem.golangmodules

%changelog
%autochangelog
