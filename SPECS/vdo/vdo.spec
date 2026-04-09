# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        Management tools for Virtual Data Optimizer
Name:           vdo
Version:        8.3.2.1
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://github.com/dm-vdo/vdo
#!RemoteAsset
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  VDO_VERSION=%{version}
BuildOption(install):  INSTALLOWNER=
BuildOption(install):  name=%{name}
BuildOption(install):  bindir=%{_bindir}
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  defaultdocdir=%{_defaultdocdir}
BuildOption(install):  libexecdir=%{_libexecdir}
BuildOption(install):  presetdir=%{_presetdir}
BuildOption(install):  python3_sitelib=/%{python3_sitelib}
BuildOption(install):  sysconfdir=%{_sysconfdir}
BuildOption(install):  unitdir=%{_unitdir}

# https://github.com/dm-vdo/vdo/issues/69
# Fix cast-align error on riscv64
Patch0:         0001-riscv64-remove-Wcast-align.patch

BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(devmapper-event)
BuildRequires:  util-linux-devel
BuildRequires:  make
%ifarch %{valgrind_arches}
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bash-completion

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space management tools for VDO.

%package        support
Summary:        Support tools for Virtual Data Optimizer
Requires:       libuuid

%description    support
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space support tools for VDO.

%conf
# No configuration needed

# no tests
%check

%files
%license COPYING
%{_bindir}/vdocalculatesize
%{_bindir}/vdoforcerebuild
%{_bindir}/vdoformat
%{_bindir}/vdostats
%{bash_completions_dir}/vdostats
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%dir %{_defaultdocdir}/%{name}/examples/monitor
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_logicalSpace.pl
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_physicalSpace.pl
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_savingPercent.pl
%{_mandir}/man8/vdocalculatesize.8*
%{_mandir}/man8/vdoforcerebuild.8*
%{_mandir}/man8/vdoformat.8*
%{_mandir}/man8/vdostats.8*

%files support
%license COPYING
%{_bindir}/adaptlvm
%{_bindir}/vdoaudit
%{_bindir}/vdodebugmetadata
%{_bindir}/vdodumpblockmap
%{_bindir}/vdodumpmetadata
%{_bindir}/vdolistmetadata
%{_bindir}/vdoreadonly
%{_bindir}/vdorecover
%{_mandir}/man8/adaptlvm.8*
%{_mandir}/man8/vdoaudit.8*
%{_mandir}/man8/vdodebugmetadata.8*
%{_mandir}/man8/vdodumpblockmap.8*
%{_mandir}/man8/vdodumpmetadata.8*
%{_mandir}/man8/vdolistmetadata.8*
%{_mandir}/man8/vdoreadonly.8*
%{_mandir}/man8/vdorecover.8*

%changelog
%autochangelog
