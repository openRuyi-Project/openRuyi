# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           columnize
%define go_import_path  github.com/ryanuber/columnize
%define commit_id       9b3edd62028f107d7cabb19353292afd29311a4e

Name:           go-github-ryanuber-columnize
Version:        0+git20260624.9b3edd6
Release:        %autorelease
Summary:        Easy column-formatted output for Go
License:        MIT
URL:            https://github.com/ryanuber/columnize
#!RemoteAsset:  sha256:eed20c1d22138359ef2fe0908fc47b19a15108b66b36b6f30365dfd22bee1dec
Source0:        https://github.com/ryanuber/columnize/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream version serf pins predates any release tag, so build from the
# pinned commit.
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ryanuber/columnize) = %{version}

%description
columnize formats lists of data into aligned columns of text. It is used by
the hashicorp/serf agent CLI for tabular output.

%files
%doc README*
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
