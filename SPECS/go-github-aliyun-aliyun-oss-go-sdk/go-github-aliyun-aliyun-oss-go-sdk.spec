# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aliyun-oss-go-sdk
%define go_import_path  github.com/aliyun/aliyun-oss-go-sdk
# TODO: test dependency need too much dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-aliyun-aliyun-oss-go-sdk
Version:        3.0.2
Release:        %autorelease
Summary:        Aliyun OSS SDK for Go
License:        MIT
URL:            https://github.com/aliyun/aliyun-oss-go-sdk
#!RemoteAsset
Source0:        https://github.com/aliyun/aliyun-oss-go-sdk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aliyun/aliyun-oss-go-sdk) = %{version}

%description
* This Go SDK is based on the official APIs of Alibaba Cloud OSS
(http://www.aliyun.com/product/oss/).
* Alibaba Cloud Object Storage Service (OSS) is a cloud storage
service provided by Alibaba Cloud, featuring massive capacity,
security, a low cost, and high reliability.
* The OSS can store any type of files and therefore applies to
various
websites, development enterprises and developers.
* With this SDK, you can upload, download and manage data on any app
anytime and anywhere conveniently.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
