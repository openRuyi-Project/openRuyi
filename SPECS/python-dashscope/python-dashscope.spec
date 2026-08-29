# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dashscope

Name:           python-%{srcname}
Version:        1.25.11
Release:        %autorelease
Summary:        DashScope Python SDK for Alibaba Cloud Model Studio
License:        Apache-2.0
URL:            https://dashscope.aliyun.com/
VCS:            git:https://github.com/dashscope/dashscope-sdk-python
# PyPI source not available for this version, using GitHub release
#!RemoteAsset:  sha256:1279d8d09552184c9ccdd85bf89d08058e66c4697b9441c862fbdbf671d34d5f
Source0:        https://github.com/dashscope/dashscope-sdk-python/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(websocket-client)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
DashScope is the official SDK for Python provided by Alibaba Cloud Model Studio.
It provides access to AI models and services from Alibaba Cloud, particularly
the Qwen series of models. The SDK supports text generation, multimodal
embeddings, streaming responses, and API key authentication for Alibaba Cloud
services.

%prep -a
sed -i 's/version=get_version(),/version="%{version}",/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
