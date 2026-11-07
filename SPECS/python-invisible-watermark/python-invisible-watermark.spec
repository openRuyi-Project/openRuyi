# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname invisible-watermark
%global commit 85b10745cfa3849411af22375a847fba36d405ed

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        Invisible image watermarking algorithms
License:        MIT
URL:            https://github.com/ShieldMnt/invisible-watermark
#!RemoteAsset:  sha256:ca4e978d807a89dd96169ccabc5e98583cf676344bcca01aad095db71f6ea514
Source0:        https://github.com/ShieldMnt/invisible-watermark/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Patch2000:      2000-Use-the-system-OpenCV-distribution-name.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(prep):  -n %{srcname}-%{commit} -p1

BuildOption(install):  imwatermark

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Invisible-watermark encodes and decodes image watermarks using discrete
wavelet transforms, discrete cosine transforms, and neural networks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/invisible-watermark

%changelog
%autochangelog
