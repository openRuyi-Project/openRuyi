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
#!RemoteAsset
Source0:        https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  expat

%description
Abstractions to extract information from the Linux kernel /proc files.

%package     -n python3-linux-procfs
Summary:     %{summary}
%python_provide python3-linux-procfs
Requires:    python3-six

%description -n python3-linux-procfs
Abstractions to extract information from the Linux kernel /proc files.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
#rm -rf %{buildroot}
%pyproject_install

%files -n python3-linux-procfs
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python3_sitelib}/procfs/
%defattr(0644,root,root,0755)
%{python3_sitelib}/python_linux_procfs*.dist-info
%license COPYING

%changelog
%autochangelog
