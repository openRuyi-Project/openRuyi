# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname groovy

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Groovy is a Python-to-JavaScript transpiler
License:        Apache-2.0
URL:            https://github.com/gradio-app/groovy
#!RemoteAsset:  sha256:25c1dc09b3f9d7e292458aa762c6beb96ea037071bf5e917fc81fb78d2231083
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A small Python library created to help developers protect their
applications from Server Side Request Forgery (SSRF) attacks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
