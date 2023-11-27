#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v2
# autospec commit: e661f3a
#
Name     : pypi-cloudflare
Version  : 2.14.2
Release  : 41
URL      : https://files.pythonhosted.org/packages/fd/ad/f3df6ba6e289d468c9c92b4295d9e3ff988e0b85d126f3a525be1bce6d9e/cloudflare-2.14.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/ad/f3df6ba6e289d468c9c92b4295d9e3ff988e0b85d126f3a525be1bce6d9e/cloudflare-2.14.2.tar.gz
Summary  : Python wrapper for the Cloudflare v4 API
Group    : Development/Tools
License  : MIT
Requires: pypi-cloudflare-bin = %{version}-%{release}
Requires: pypi-cloudflare-license = %{version}-%{release}
Requires: pypi-cloudflare-man = %{version}-%{release}
Requires: pypi-cloudflare-python = %{version}-%{release}
Requires: pypi-cloudflare-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(jsonlines)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# cloudflare-python
## Installation
Two methods are provided to install this software.
Use PyPi (see [package](https://pypi.python.org/pypi/cloudflare) details) or GitHub (see [package](https://github.com/cloudflare/python-cloudflare) details).

%package bin
Summary: bin components for the pypi-cloudflare package.
Group: Binaries
Requires: pypi-cloudflare-license = %{version}-%{release}

%description bin
bin components for the pypi-cloudflare package.


%package license
Summary: license components for the pypi-cloudflare package.
Group: Default

%description license
license components for the pypi-cloudflare package.


%package man
Summary: man components for the pypi-cloudflare package.
Group: Default

%description man
man components for the pypi-cloudflare package.


%package python
Summary: python components for the pypi-cloudflare package.
Group: Default
Requires: pypi-cloudflare-python3 = %{version}-%{release}

%description python
python components for the pypi-cloudflare package.


%package python3
Summary: python3 components for the pypi-cloudflare package.
Group: Default
Requires: python3-core
Provides: pypi(cloudflare)
Requires: pypi(beautifulsoup4)
Requires: pypi(jsonlines)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the pypi-cloudflare package.


%prep
%setup -q -n cloudflare-2.14.2
cd %{_builddir}/cloudflare-2.14.2
pushd ..
cp -a cloudflare-2.14.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701097539
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cloudflare
cp %{_builddir}/cloudflare-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cloudflare/1857fba4ea5c0240235ad8374c2a15727733798e || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
sitedir=$(python -c "import sys; print(sys.path[-1])")
rm -rf %{buildroot}/${sitedir}/examples
man1dir=%{buildroot}/usr/share/man/man1
mkdir -pv $man1dir
#mv -v %{buildroot}/usr/man/man1/cli4.man $man1dir/cli4.1
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cli4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cloudflare/1857fba4ea5c0240235ad8374c2a15727733798e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cli4.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
