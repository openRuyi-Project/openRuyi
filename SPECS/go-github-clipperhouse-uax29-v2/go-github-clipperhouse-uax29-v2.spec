# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uax29
%define go_import_path  github.com/clipperhouse/uax29/v2
%define go_test_exclude_glob github.com/clipperhouse/uax29/v2/internal/gen*

Name:           go-github-clipperhouse-uax29-v2
Version:        2.3.0
Release:        %autorelease
Summary:        A tokenizer based on Unicode text segmentation (UAX #29), for Go. Split graphemes, words, sentences.
License:        MIT
URL:            https://github.com/clipperhouse/uax29
#!RemoteAsset
Source0:        https://github.com/clipperhouse/uax29/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/stringish)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(github.com/blevesearch/segment)
BuildRequires:  go(github.com/rivo/uniseg)

Provides:       go(github.com/clipperhouse/uax29/v2) = %{version}

Requires:       go(github.com/clipperhouse/stringish)
Requires:       go(golang.org/x/text)
Requires:       go(github.com/blevesearch/segment)
Requires:       go(github.com/rivo/uniseg)

%description
This package tokenizes (splits) words, sentences and graphemes, based on
Unicode text segmentation (https://unicode.org/reports/tr29/).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
