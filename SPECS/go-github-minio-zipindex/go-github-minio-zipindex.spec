# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zipindex
%define go_import_path  github.com/minio/zipindex

Name:           go-github-minio-zipindex
Version:        0.5.0
Release:        %autorelease
Summary:        Package for indexing zip files and storing a compressed index
License:        Apache-2.0
URL:            https://github.com/minio/zipindex
#!RemoteAsset
Source0:        https://github.com/minio/zipindex/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(github.com/philhofer/fwd)

Provides:       go(github.com/minio/zipindex) = %{version}

Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/tinylib/msgp)

%description
zipindex provides a size optimized representation of a zip file
directory to allow decompressing files inside a ZIP file without reading
the file index every file.

It will only provide the minimal needed data for successful
decompression and CRC checks.

Custom metadata can be stored per file and filtering can be performed on
the incoming files.

Currently, up to 100 million files per zip file is supported. If a
streaming format is added, this limit may be lifted.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
