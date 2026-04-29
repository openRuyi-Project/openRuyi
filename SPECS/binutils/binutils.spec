# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Do not set this in cflags to avoid test failures. Instead, use the LTO option
# provided by binutils.
%global _lto_cflags %{nil}

%bcond bootstrap 1

Name:           binutils
Summary:        GNU Binutils
License:        GFDL-1.3-only AND GPL-3.0-or-later
Version:        2.46.0
Release:        %autorelease
URL:            https://www.gnu.org/software/binutils/
VCS:            git:https://sourceware.org/git/binutils-gdb.git
#!RemoteAsset:  sha256:0f3152632a2a9ce066f20963e9bb40af7cf85b9b6c409ed892fd0676e84ecd12
Source0:        https://ftpmirror.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(build):  -C build-dir

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
# for the testsuite
BuildRequires:  glibc-static
BuildRequires:  texinfo
BuildRequires:  zlib-ng-compat-static
BuildRequires:  pkgconfig(libzstd)

Requires(post):  update-alternatives
Requires(preun):  update-alternatives

%description
C compiler utilities: ar, as, gprof, ld, nm, objcopy, objdump, ranlib,
size, strings, and strip. These utilities are needed whenever you want
to compile a program or kernel.

%package        devel
Summary:        GNU binutils (BFD development files)
License:        GPL-3.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(zlib)
Requires:       pkgconfig(libzstd)
Provides:       binutils:%{_includedir}/bfd.h

%description    devel
This package includes header files and static libraries necessary to
build programs which use the GNU BFD library, which is part of
binutils.

%conf
# FIXME: upstream problem with C23.
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
      --enable-lto \
%if %{with bootstrap} && 0%{?do_profiling}
      --enable-pgo-build=lto \
%endif
      --disable-gprofng \
      --enable-colored-disassembly \
      --disable-werror
%undefine _configure


%install
cd build-dir
make DESTDIR=%{buildroot} install-info install
make DESTDIR=%{buildroot} install-bfd install-opcodes
if [ ! -f "%{buildroot}/%{_bindir}/ld.bfd" ]; then
  mv "%{buildroot}/%{_bindir}"/{ld,ld.bfd};
else
  rm -f "%{buildroot}/%{_bindir}/ld";
fi
mkdir -p "%{buildroot}/%{_sysconfdir}/alternatives";
# Keep older versions of brp-symlink happy
ln -s "%{_sysconfdir}/alternatives/ld" "%{buildroot}/%{_bindir}/ld";

chmod a+x %{buildroot}%{_libdir}/libbfd-*
chmod a+x %{buildroot}%{_libdir}/libopcodes-*
# No shared linking outside binutils
rm %{buildroot}%{_libdir}/lib{bfd,opcodes}.so
# Remove unwanted files to shut up rpm
rm -f %{buildroot}%{_infodir}/configure* $RPM_BUILD_ROOT%{_infodir}/standards.info*
rm -f %{buildroot}%{_mandir}/man1/dlltool.1 $RPM_BUILD_ROOT%{_mandir}/man1/windres.1 $RPM_BUILD_ROOT%{_mandir}/man1/windmc.1
cd ..

%find_lang %{name} --all-name --generate-subpackages

%check
# Delete upsteam known failure. https://sourceware.org/bugzilla//show_bug.cgi?id=32983
sed -i '/"pr19719/d' ld/testsuite/ld-elf/shared.exp

cd build-dir

# Increase timeout to fit slow qemu-system builder.
make RUNTESTFLAGS='TEST_TIMEOUT=600' check

%post
if [ "$1" = 1 ]; then
update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.bfd 2
fi

%preun
if [ "$1" = 0 ]; then
     update-alternatives --remove ld %{_bindir}/ld.bfd
fi;

%files
%defattr(-,root,root)
%dir %{_prefix}/%{_host}
%dir %{_prefix}/%{_host}/lib
%{_prefix}/%{_host}/bin/*
%{_prefix}/%{_host}/lib/ldscripts
%{_libdir}/libsframe.so.*
%{_libdir}/libctf.so.*
%{_libdir}/libctf-nobfd.so.*
%dir %{_libdir}/bfd-plugins
%{_libdir}/bfd-plugins/libdep.so
%{_bindir}/*
%ghost %{_sysconfdir}/alternatives/ld
%doc %{_infodir}/*.gz
%{_libdir}/lib*-%{version}*.so
%doc %{_mandir}/man1/*.1.gz

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/lib*.*a
%{_libdir}/libctf.so
%{_libdir}/libctf-nobfd.so
%{_libdir}/libsframe.so

%changelog
%autochangelog
