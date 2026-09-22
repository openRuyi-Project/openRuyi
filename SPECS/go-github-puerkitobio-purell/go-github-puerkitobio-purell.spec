# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           purell
%define go_import_path  github.com/PuerkitoBio/purell

Name:           go-github-puerkitobio-purell
Version:        1.1.1
Release:        %autorelease
Summary:        Go library for purell
License:        BSD-3-Clause
URL:            https://github.com/PuerkitoBio/purell
VCS:            git:https://github.com/PuerkitoBio/purell.git
#!RemoteAsset:  sha256:93e2ae2b12fc656ecc7ca28336009d24431247d2af59949c59fdef26ecc9a971
Source0:        https://github.com/PuerkitoBio/purell/archive/v1.1.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n purell-1.1.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/PuerkitoBio/urlesc)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/PuerkitoBio/purell) = %{version}

Requires:       go(github.com/PuerkitoBio/urlesc)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)

%description
This package provides the github.com/PuerkitoBio/purell Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
