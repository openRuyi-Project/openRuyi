# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-linux-procfs
Version:        0.7.4
Release:        %autorelease
Summary:        Linux /proc abstraction classes
License:        GPL-2.0-only
URL:            https://rt.wiki.kernel.org/index.php/Tuna
#!RemoteAsset:  sha256:3a15e97b5e19279978e9aab5567416d76b8101f2cc82f95aca0f6f2dade4fbd7
Source0:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l procfs

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-linux-procfs
%python_provide python3-linux-procfs

Requires:       python3dist(six)

%description
Abstractions to extract information from the Linux kernel /proc files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING
%attr(0755,root,root) %{_bindir}/pflags

%changelog
%autochangelog
