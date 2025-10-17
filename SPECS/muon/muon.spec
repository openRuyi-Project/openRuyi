# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           muon
Version:        0.6.0
Release:        %autorelease
Summary:        Meson build system alternative implementation in C99
License:        Apache-2.0 AND GPL-3.0-only AND MIT AND Unlicense
URL:            https://muon.build/
VCS:            git:https://github.com/muon-build/muon
#!RemoteAsset:  sha256:5300e58c4b4d43e3026856004c79d746075aaa9d9e66d76ba9f32ce249495b81
Source0:        https://github.com/muon-build/muon/archive/refs/tags/%{version}.tar.gz
Source1:        macros.muon

BuildRequires:  samurai-ninja

Requires:       samurai-ninja

%description
Muon is an implementation of the meson build system in c99
with minimal dependencies.

%prep
%autosetup

%build
export CC=%{__cc}
export CFLAGS="%{optflags} -DBOOTSTRAP_NO_SAMU"
./bootstrap.sh %{_vpath_builddir}
%{_vpath_builddir}/muon-bootstrap \
 setup \
 -Dsamurai=disabled \
 -Dprefix=%{_prefix} \
 -Dlibdir=%{_lib} \
 -Dincludedir=%{_includedir} \
 -Dlibexecdir=%{_libexecdir} \
 -Dsbindir=%{_sbindir} \
 %{_vpath_builddir}
ninja -C %{_vpath_builddir}
%{_vpath_builddir}/muon \
    setup -Dsamurai=disabled \
    -Dprefix=%{_prefix} \
    -Dlibdir=%{_lib} \
    -Dincludedir=%{_includedir} \
    -Dlibexecdir=%{_libexecdir} \
    -Dsbindir=%{_sbindir} \
    %{_vpath_builddir}
ninja -C %{_vpath_builddir}

%check
%{_vpath_builddir}/muon -C %{_vpath_builddir} test

%install
DESTDIR=%{buildroot} %{_vpath_builddir}/muon -C %{_vpath_builddir} install
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_rpmmacrodir}/macros.muon

%files
%doc README.md
%license LICENSES/*
%{_bindir}/muon
%{_datadir}/man/man1/muon.1.*
%{_datadir}/man/man3/meson-reference.3.*
%{_rpmmacrodir}/macros.muon

%changelog
%autochangelog
