# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           highwayhash
%define go_import_path  github.com/minio/highwayhash

Name:           go-github-minio-highwayhash
Version:        1.0.3
Release:        %autorelease
Summary:        Native Go version of HighwayHash with optimized assembly implementations on Intel and ARM. Able to process over 10 GB/sec on a single core on Intel CPUs - https://en.wikipedia.org/wiki/HighwayHash
License:        Apache-2.0
URL:            https://github.com/minio/highwayhash
#!RemoteAsset
Source0:        https://github.com/minio/highwayhash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/minio/highwayhash) = %{version}

Requires:       go(golang.org/x/sys)

%description
HighwayHash

HighwayHash (https://github.com/google/highwayhash) is a pseudo-random-
function (PRF) developed by Jyrki Alakuijala, Bill Cox and Jan
Wassenberg (Google research). HighwayHash takes a 256 bit key and
computes 64, 128 or 256 bit hash values of given messages.

It can be used to prevent hash-flooding attacks or authenticate short-
lived messages. Additionally it can be used as a fingerprinting
function. HighwayHash is not a general purpose cryptographic hash
function (such as Blake2b, SHA-3 or SHA-2) and should not be used if
strong collision resistance is required.

This repository contains a native Go version and optimized assembly
implementations for Intel, ARM and ppc64le architectures.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
