# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-homedir
%define go_import_path  github.com/mitchellh/go-homedir

Name:           go-github-mitchellh-go-homedir
Version:        1.1.0
Release:        %autorelease
Summary:        Go library for detecting and expanding the user's home directory without cgo.
License:        MIT
URL:            https://github.com/mitchellh/go-homedir
#!RemoteAsset
Source0:        https://github.com/mitchellh/go-homedir/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/go-homedir) = %{version}

%description
This is a Go library for detecting the user's home directory without the
use of cgo, so the library can be used in cross-compilation environments.

Usage is incredibly simple, just call homedir.Dir() to get the home
directory for a user, and homedir.Expand() to expand the ~ in a path to
the home directory.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
