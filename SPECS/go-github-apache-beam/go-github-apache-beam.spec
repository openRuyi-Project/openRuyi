# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           beam
%define go_import_path  github.com/apache/beam
# TODO: check circular dependency - Julian
%define go_test_ignore_failure 1

Name:           go-github-apache-beam
Version:        2.71.0
Release:        %autorelease
Summary:        Apache Beam is a unified programming model for Batch and Streaming data processing.
License:        Apache-2.0
URL:            https://github.com/apache/beam
#!RemoteAsset
Source0:        https://github.com/apache/beam/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apache/beam) = %{version}

%description
Apache Beam (http://beam.apache.org/) is a unified model for defining
both batch and streaming data-parallel processing pipelines, as well as
a
set of language-specific SDKs for constructing pipelines and Runners for
executing them on distributed processing backends, including Apache
Flink (http://flink.apache.org/), Apache Spark
(http://spark.apache.org/), Google Cloud Dataflow
(http://cloud.google.com/dataflow/), and Hazelcast Jet
(https://hazelcast.com/).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
