#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ICSNP
Version  : 1.1.1
Release  : 18
URL      : https://cran.r-project.org/src/contrib/ICSNP_1.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ICSNP_1.1-1.tar.gz
Summary  : Tools for Multivariate Nonparametrics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ICSNP-lib = %{version}-%{release}
Requires: R-ICS
Requires: R-mvtnorm
BuildRequires : R-ICS
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-ICSNP package.
Group: Libraries

%description lib
lib components for the R-ICSNP package.


%prep
%setup -q -c -n ICSNP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552893075

%install
export SOURCE_DATE_EPOCH=1552893075
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICSNP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICSNP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICSNP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ICSNP || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ICSNP/ChangeLog
/usr/lib64/R/library/ICSNP/DESCRIPTION
/usr/lib64/R/library/ICSNP/INDEX
/usr/lib64/R/library/ICSNP/Meta/Rd.rds
/usr/lib64/R/library/ICSNP/Meta/data.rds
/usr/lib64/R/library/ICSNP/Meta/features.rds
/usr/lib64/R/library/ICSNP/Meta/hsearch.rds
/usr/lib64/R/library/ICSNP/Meta/links.rds
/usr/lib64/R/library/ICSNP/Meta/nsInfo.rds
/usr/lib64/R/library/ICSNP/Meta/package.rds
/usr/lib64/R/library/ICSNP/NAMESPACE
/usr/lib64/R/library/ICSNP/R/ICSNP
/usr/lib64/R/library/ICSNP/R/ICSNP.rdb
/usr/lib64/R/library/ICSNP/R/ICSNP.rdx
/usr/lib64/R/library/ICSNP/data/LASERI.txt.gz
/usr/lib64/R/library/ICSNP/data/pulmonary.rda
/usr/lib64/R/library/ICSNP/help/AnIndex
/usr/lib64/R/library/ICSNP/help/ICSNP.rdb
/usr/lib64/R/library/ICSNP/help/ICSNP.rdx
/usr/lib64/R/library/ICSNP/help/aliases.rds
/usr/lib64/R/library/ICSNP/help/paths.rds
/usr/lib64/R/library/ICSNP/html/00Index.html
/usr/lib64/R/library/ICSNP/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ICSNP/libs/ICSNP.so
/usr/lib64/R/library/ICSNP/libs/ICSNP.so.avx2
/usr/lib64/R/library/ICSNP/libs/ICSNP.so.avx512
