# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# disable libalternatives for now until it's changed to not
# introduce cmake/cunit-tests into the bootstrap cycle
%bcond libalternatives 0

%bcond bootstrap 1

Name:           binutils
Summary:        GNU Binutils
License:        GFDL-1.3-only AND GPL-3.0-or-later
Version:        2.45
Release:        %autorelease
URL:            https://www.gnu.org/software/binutils/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2.sig
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
# for the testsuite
BuildRequires:  glibc-static
BuildRequires:  texinfo
BuildRequires:  zlib-devel-static
BuildRequires:  libzstd-devel
%if %{with libalternatives}
Requires:       alts
%else
PreReq:         update-alternatives
%endif

BuildSystem:  autotools
BuildOption(build): -C build-dir

%description
C compiler utilities: ar, as, gprof, ld, nm, objcopy, objdump, ranlib,
size, strings, and strip. These utilities are needed whenever you want
to compile a program or kernel.

%package devel
Summary:        GNU binutils (BFD development files)
License:        GPL-3.0-or-later
Requires:       binutils = %{version}-%{release}
Requires:       zlib-devel
Requires:       libzstd-devel
Provides:       binutils:${%_includedir}/bfd.h

%description devel
This package includes header files and static libraries necessary to
build programs which use the GNU BFD library, which is part of
binutils.

%conf
%define _configure ../configure
mkdir build-dir
cd build-dir
%configure --with-bugurl=%{_vendor_bug_url} \
      --with-separate-debug-dir=%{_prefix}/lib/debug \
      --with-pic --with-system-zlib \
      --enable-plugins \
      --enable-threads \
      --enable-compressed-debug-sections=gas \
      --enable-new-dtags \
      --enable-default-hash-style=both \
    --enable-compressed-debug-sections=all \
      --enable-shared \
%if %{with bootstrap} && 0%{?do_profiling}
      --enable-pgo-build=lto \
%endif
      --enable-colored-disassembly
%undefine _configure


%install
cd build-dir
make DESTDIR=%{buildroot} install-info install
make DESTDIR=%{buildroot} install-bfd install-opcodes
if [ ! -f "%{buildroot}/%_bindir/ld.bfd" ]; then
  mv "%{buildroot}/%_bindir"/{ld,ld.bfd};
else
  rm -f "%{buildroot}/%_bindir/ld";
fi
%if ! 0%{with libalternatives}
mkdir -p "%{buildroot}/%_sysconfdir/alternatives";
# Keep older versions of brp-symlink happy
ln -s "%_sysconfdir/alternatives/ld" "%{buildroot}/%_bindir/ld";
%else
ln -s %{_bindir}/alts "%{buildroot}/%_bindir/ld";
mkdir -p %{buildroot}%{_datadir}/libalternatives/ld;
cat > %{buildroot}%{_datadir}/libalternatives/ld/1.conf <<EOF
binary=%{_bindir}/ld.bfd
EOF
%endif

chmod a+x %{buildroot}%{_libdir}/libbfd-*
chmod a+x %{buildroot}%{_libdir}/libopcodes-*
# No shared linking outside binutils
rm %{buildroot}%{_libdir}/lib{bfd,opcodes}.so
rm %{buildroot}%{_libdir}/lib{bfd,opcodes,ctf,ctf-nobfd}.la
rm -f %{buildroot}%{_libdir}/gprofng/lib*.{l,}a
# Remove unwanted files to shut up rpm
rm -f %{buildroot}%{_infodir}/configure* $RPM_BUILD_ROOT%{_infodir}/standards.info*
rm -f %{buildroot}%{_mandir}/man1/dlltool.1 $RPM_BUILD_ROOT%{_mandir}/man1/windres.1 $RPM_BUILD_ROOT%{_mandir}/man1/windmc.1
cd ..

%find_lang %{name} --all-name --generate-subpackages

%post
%if ! %{with libalternatives}
"%_sbindir/update-alternatives" --install \
     "%_bindir/ld" ld "%_bindir/ld.bfd" 2
%endif

%if %{with libalternatives}
%pre
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
     "%_sbindir/update-alternatives" --remove ld "%_bindir/ld.bfd";
fi;
%endif

%preun
%if ! %{with libalternatives}
if [ "$1" = 0 ]; then
     "%_sbindir/update-alternatives" --remove ld "%_bindir/ld.bfd";
fi;
%endif

%files
%defattr(-,root,root)
%{_prefix}/%{_host}/bin/*
%{_prefix}/%{_host}/lib/ldscripts
%{_libdir}/libsframe.so.*
%{_libdir}/libgprofng.so.*
%{_libdir}/libctf.so.*
%{_libdir}/libctf-nobfd.so.*
%dir %{_libdir}/bfd-plugins
%{_libdir}/bfd-plugins/libdep.so
%{_bindir}/*
%if ! 0%{with libalternatives}
%ghost %_sysconfdir/alternatives/ld
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/ld
%{_datadir}/libalternatives/ld/2.conf
%endif
%doc %{_infodir}/*.gz
%{_libdir}/lib*-%{version}*.so
%doc %{_mandir}/man1/*.1.gz
%dir %{_libdir}/gprofng/
%{_libdir}/gprofng/lib*.so
%{_sysconfdir}/gprofng.rc

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/lib*.*a
%{_libdir}/libctf.so
%{_libdir}/libctf-nobfd.so
%{_libdir}/libsframe.so
%{_libdir}/libgprofng.so
%{_docdir}/gprofng/*

%changelog
%{?autochangelog}
