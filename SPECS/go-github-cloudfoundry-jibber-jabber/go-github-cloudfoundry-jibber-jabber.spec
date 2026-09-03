# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jibber_jabber
%define go_import_path  github.com/cloudfoundry/jibber_jabber
%define commit_id       bcc4c8345a21301bf47c032ff42dd1aae2fe3027

Name:           go-github-cloudfoundry-jibber-jabber
Version:        0+git20260621.bcc4c83
Release:        %autorelease
Summary:        Cross Platform locale detection for Golang
License:        Apache-2.0
URL:            https://github.com/cloudfoundry/jibber_jabber
#!RemoteAsset:  sha256:90ce9900057a28b83a95a91562244fc6b24420507fce1ead1d1325a61495cea3
Source0:        https://github.com/cloudfoundry/jibber_jabber/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cloudfoundry/jibber_jabber) = %{version}

%description
jibber_jabber detects the operating system's configured language and locale.

# Test suite depends on ginkgo/gomega; drop it (library has no runtime deps).
%prep -a
rm -f *_test.go

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
