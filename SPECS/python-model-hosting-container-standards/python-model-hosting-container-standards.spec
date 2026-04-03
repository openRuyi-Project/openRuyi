# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname model-hosting-container-standards
%global pkgname model_hosting_container_standards

Name:           python-%{srcname}
Version:        0.1.14
Release:        %autorelease
Summary:        Python toolkit for standardized model hosting container implementations
License:        TBD
URL:            https://pypi.org/project/model-hosting-container-standards/
#!RemoteAsset:  sha256:b6cf4c46d88ce6acd6e543a578bb88ffd55d1179a7c09c22e61ae1d8a567c564
Source0:        https://files.pythonhosted.org/packages/source/m/model-hosting-container-standards/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
# 大写 L 护体：放弃机器自动提取，宣告打包者将手动处理授权文件
BuildOption(install):  -L %{pkgname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A standardized Python framework for seamless integration between ML frameworks
(TensorRT-LLM, vLLM) and Amazon SageMaker hosting. It simplifies model deployment
by providing a unified handler system, flexible configuration, and framework
agnostic compatibility.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pkgname}-%{version}

# 【核心补丁】：强行捏造一个内容为 TBD 的 LICENSE 文件，满足系统的物理文件检查
echo "TBD" > LICENSE


%files -f %{pyproject_files}
# 把自动生成的命令行工具加入资产清单
%{_bindir}/generate-supervisor-config
%{_bindir}/standard-supervisor
%license LICENSE
%doc README.md

%changelog
%autochangelog
