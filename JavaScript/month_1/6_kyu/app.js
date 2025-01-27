function solution (roman) {
  	const roman_tt = {
		    "MM":2000,
			"MDCLXVI":1666,
			"M":1000,
			"CD":400,
			"XC":90,
			"XL":40,
			"I":1,
			"V":5,
			"X":10,
			"L":50,
			"C":100,
			"D":500,
	}
	let result = 0
	for(let i=0;i<roman.length;i++){
		const current = roman_tt[roman[i]];
		const next =roman_tt[roman[i+1]];
		if (next && current < next){
			result += next - current;
			i++;
		}else{
			result+=current;
		}

	}

	return result;
}
console.log(solution("MMVIII"))