# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ssh_config
%define go_import_path  github.com/kevinburke/ssh_config

Name:           go-github-kevinburke-ssh-config
Version:        1.6.0
Release:        %autorelease
Summary:        Parser for OpenSSH ssh_config files
License:        MIT
URL:            https://github.com/kevinburke/ssh_config
#!RemoteAsset:  sha256:bb9dbfe0b9f49eebaab82695103f395b1ae553c2b80501b22089a419774910e3
Source0:        https://github.com/kevinburke/ssh_config/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fixture tests exercise explicit testdata as the user config. Keep them
# hermetic so host /etc/ssh/ssh_config read errors cannot mask those fixtures.
# - HNO3Miracle
Patch2000:      2000-make-fixture-tests-ignore-system-config.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kevinburke/ssh_config) = %{version}

%description
ssh_config parses OpenSSH client configuration files while preserving comments,
making it useful for reading and editing SSH configuration from Go programs.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
