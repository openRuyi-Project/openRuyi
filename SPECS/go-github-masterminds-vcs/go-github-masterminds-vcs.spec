# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vcs
%define go_import_path  github.com/Masterminds/vcs

Name:           go-github-masterminds-vcs
Version:        1.11.1
Release:        %autorelease
Summary:        Work with Git, Mercurial, Bazaar, and Subversion repositories
License:        MIT
URL:            https://github.com/Masterminds/vcs
#!RemoteAsset:  sha256:522715a220b464de1fce808e5353261e9d1cd1ca16680bccf3f67ce94a6b4087
Source0:        https://github.com/Masterminds/vcs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream's remaining tests require network access to obsolete external
# repositories or Bazaar, Mercurial, and Subversion commands not in openRuyi.
# Keep the local Git and error-handling tests active.
BuildOption(check):  -run '^(TestNewRemoteError|TestNewLocalError|TestGitCheckLocal|TestGitInit|TestDepInstalled|TestVCSFileLookup)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  git

Provides:       go(github.com/Masterminds/vcs) = %{version}

%description
This Go library provides a common interface for repository operations
across Git, Mercurial, Bazaar, and Subversion. Helm 2 uses it for chart
plugin installation.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
