# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
%global archdir riscv
%endif
%ifarch x86_64
%global archdir x86_64
%endif

Name:           linux-headers
Version:        6.18.18
Release:        %autorelease
Summary:        Header files for the Linux kernel for use by userspace
License:        GPL-2.0-only AND LGPL-2.1-only AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.kernel.org/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
#!RemoteAsset:  sha256:f4855f382c1b735c84072bdef36db5bcd5dc7b0c37e42f5104317149a0a486ef
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

BuildRequires:  rsync

%description
Linux-headers includes the C header files that specify the stable API
interface between the Linux kernel and userspace libraries and programs.

%prep
%autosetup -p1 -n linux-%{version}

%install
%make_build ARCH=%{archdir} headers_install INSTALL_HDR_PATH=%{buildroot}%{_prefix}

%files
%license COPYING
%{_includedir}/*

%changelog
%autochangelog
