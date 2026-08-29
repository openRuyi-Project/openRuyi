# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           maxminddb-golang
%define go_import_path  github.com/oschwald/maxminddb-golang
%global testdata_commit 3e225a82e492a58eef738ef2b6e94aa4f50ef932

Name:           go-github-oschwald-maxminddb-golang
Version:        1.13.1
Release:        %autorelease
Summary:        MaxMind DB reader for Go
License:        ISC AND CC-BY-SA-3.0
URL:            https://github.com/oschwald/maxminddb-golang
VCS:            git:https://github.com/oschwald/maxminddb-golang
#!RemoteAsset:  sha256:d337efdac8d906cf3853f048fb74f96ecff4f70c2e64d869fdd87c83eb797bfd
Source0:        https://github.com/oschwald/maxminddb-golang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1 only restores the exact MaxMind-DB test-data submodule commit pinned
# by upstream.
#!RemoteAsset:  sha256:d73bcaaa6f96ffe06e6dcdb843cf43b5eb8dbebaec8361fce352ecc61c04bccd
Source1:        https://github.com/maxmind/MaxMind-DB/archive/%{testdata_commit}/MaxMind-DB-%{testdata_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/oschwald/maxminddb-golang) = %{version}

Requires:       go(golang.org/x/sys)

%description
Maxminddb-golang is a Go reader for the MaxMind DB file format. It provides
memory-mapped and in-memory access to MaxMind database records.

%prep -a
rm -rf test-data
mkdir -p test-data
tar -xf %{SOURCE1} --strip-components=1 -C test-data

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
