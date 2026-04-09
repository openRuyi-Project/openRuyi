# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           color-rpm-macros
Version:        1
Release:        %autorelease
Summary:        RPM macro definitions for color
License:        Public Domain
BuildArch:      noarch

Requires:       filesystem
Requires:       rpm

%description
This package provides the directory layout used to store color profiles and
settings.

%install
mkdir -p %{buildroot}%{_datadir}/color/icc
mkdir -p %{buildroot}%{_datadir}/color/cmms
mkdir -p %{buildroot}%{_datadir}/color/settings
mkdir -p %{buildroot}%{_localstatedir}/lib/color/icc

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.color <<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF

%files
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_localstatedir}/lib/color
%dir %{_localstatedir}/lib/color/icc
%{_rpmconfigdir}/macros.d/macros.color

%changelog
%autochangelog
