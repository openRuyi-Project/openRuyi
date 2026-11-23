# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           direnv
%global go_import_path  github.com/direnv/direnv/v2
# Go's -C flag keeps the build inside the module import path for internal packages.
%global go_build_flags_default -C %{_builddir}/go/src/%{go_import_path} -v

Name:           direnv
Version:        2.38.2
Release:        %autorelease
Summary:        Environment switcher for the shell
License:        MIT
URL:            https://github.com/direnv/direnv
#!RemoteAsset:  sha256:02c5e873e9ebcf2798513f7dd3775e5b8aace99bfa1e0c1b93091b6d4cbcaffb
Source0:        https://github.com/direnv/direnv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(golang.org/x/mod)

%description
direnv is an environment switcher for the shell. It loads and unloads
directory-specific environment variables for bash, zsh, fish, tcsh and other
supported shells.

%install -p
cd %{_builddir}/go/src/%{go_import_path}

%install -a
install -d %{buildroot}%{_mandir}/man1
install -pm0644 man/*.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGELOG.md README.md docs
%license LICENSE
%{_bindir}/direnv
%{_mandir}/man1/direnv.1*
%{_mandir}/man1/direnv-fetchurl.1*
%{_mandir}/man1/direnv-stdlib.1*
%{_mandir}/man1/direnv.toml.1*

%changelog
%autochangelog
