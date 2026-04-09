# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kmeans
%define go_import_path  github.com/muesli/kmeans

Name:           go-github-muesli-kmeans
Version:        0.3.1
Release:        %autorelease
Summary:        k-means clustering algorithm implementation written in Go
License:        MIT
URL:            https://github.com/muesli/kmeans
#!RemoteAsset
Source0:        https://github.com/muesli/kmeans/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/muesli/clusters)
BuildRequires:  go(github.com/wcharczuk/go-chart)
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)

Provides:       go(github.com/muesli/kmeans) = %{version}

Requires:       go(github.com/muesli/clusters)
Requires:       go(github.com/wcharczuk/go-chart)

%description
k-means clustering algorithm implementation written in Go

k-means clustering (https://en.wikipedia.org/wiki/K-means_clustering)
partitions a multi-dimensional data set into k clusters, where each data
point belongs to the cluster with the nearest mean, serving as a
prototype of the cluster.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
