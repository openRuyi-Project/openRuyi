# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uax29
%define go_import_path  github.com/clipperhouse/uax29/v2
# internal/gen is a Unicode table generator. The comparative suites import
# other tokenizers (uniseg, bleve segment, charmbracelet ansi) that are not
# part of this library.
%define go_test_exclude_glob %{shrink:
    github.com/clipperhouse/uax29/v2/internal/gen*
    github.com/clipperhouse/uax29/v2/graphemes/comparative
    github.com/clipperhouse/uax29/v2/words/comparative
}

Name:           go-github-clipperhouse-uax29-v2
Version:        2.7.0
Release:        %autorelease
Summary:        Unicode text segmentation (UAX #29) tokenizer for Go
License:        MIT
URL:            https://github.com/clipperhouse/uax29
#!RemoteAsset:  sha256:e127ac39f501dc7c92b20b980a4a6a5766c2d95b54f9d2a0d1b2ef373817f9a0
Source0:        https://github.com/clipperhouse/uax29/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/clipperhouse/uax29/v2) = %{version}
Provides:       go(github.com/clipperhouse/uax29/v2/graphemes) = %{version}

%description
This package tokenizes words, sentences and graphemes based on Unicode text
segmentation (https://unicode.org/reports/tr29/).

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
