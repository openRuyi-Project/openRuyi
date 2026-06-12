# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# ignore the explicit bash requires from the kernel mod scripts
%define __requires_exclude ^/bin/bash$

Name:           rpm-config-openruyi
Version:        20251216
Release:        %autorelease
Summary:        specific RPM configuration files
License:        GPL-2.0-or-later
URL:            https://git.openruyi.cn/openruyi/openruyi-repo
BuildArch:      noarch

#!BuildIgnore:  rpm-config-openruyi

Provides:       rpm-config

# RPM owns the directories we need
Requires:       rpm

%sourcelist
brp-openruyi
firmware.attr
firmware.prov
macros
macros.buildsystem
macros.completions
macros.ldconfig
macros.sbat
macros.vendor
macros.vpath
rpmrc

%description
This package contains the RPM configuration data for the openruyi
distribution families.

%prep
%setup -c -T
cp -p %{sources} .

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/openruyi
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/openruyi macros
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/openruyi rpmrc

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} *.attr
install -p -m 755 -t %{buildroot}%{_rpmconfigdir} brp-openruyi
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 755 -t %{buildroot}%{_rpmconfigdir}/ *.prov
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

%files
%dir %{_rpmconfigdir}/openruyi/
%{_rpmconfigdir}/openruyi/macros
%{_rpmconfigdir}/openruyi/rpmrc
%{_rpmconfigdir}/macros.d/macros.*
%{_rpmconfigdir}/fileattrs/*
%{_rpmconfigdir}/brp-openruyi
%{_rpmconfigdir}/firmware.prov

%changelog
%autochangelog
